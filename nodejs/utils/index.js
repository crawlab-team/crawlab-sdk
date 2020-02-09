const db = require('../db')

module.exports = {
  saveItem: async (item) => {
    item['task_id'] = process.env['CRAWLAB_TASK_ID']
    const col = await db.getCollection()
    await col.insertOne(item)
  },
  close: async () => {
    const client = await db.getClient()
    await client.close()
  }
}
