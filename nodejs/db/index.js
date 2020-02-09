const mongodb = require('mongodb')
const MongoClient = mongodb.MongoClient

const MONGO_HOST = process.env['CRAWLAB_MONGO_HOST'] || 'localhost'
const MONGO_PORT = process.env['CRAWLAB_MONGO_PORT'] || 27017
const MONGO_DB = process.env['CRAWLAB_MONGO_DB']
const MONGO_USERNAME = process.env['CRAWLAB_MONGO_USERNAME']
const MONGO_PASSWORD = process.env['CRAWLAB_MONGO_PASSWORD']
const MONGO_AUTHSOURCE = process.env['CRAWLAB_MONGO_AUTHSOURCE'] || 'admin'
const COLLECTION = process.env['CRAWLAB_COLLECTION']

let client

const getClient = async () => {
  let url
  if (MONGO_USERNAME) {
    url = `mongodb://${MONGO_USERNAME}:${MONGO_PASSWORD}@${MONGO_HOST}:${MONGO_PORT}/${MONGO_DB}?authSource=${MONGO_AUTHSOURCE}`
  } else {
    url = `mongodb://${MONGO_HOST}:${MONGO_PORT}/${MONGO_DB}`
  }

  if (client === undefined) {
    client = await MongoClient.connect(url, {
      useUnifiedTopology: true
    })
  }
  return client
}

const getDb = async () => {
  const client = await getClient()
  return await client.db(MONGO_DB)
}

const getCollection = async () => {
  const db = await getDb()
  return await db.collection(COLLECTION)
}

module.exports = {
  getClient,
  getDb,
  getCollection
}
