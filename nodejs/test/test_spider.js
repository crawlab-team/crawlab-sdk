const crawlab = require('../index');

(async () => {
  for (let i = 0; i < 10; i++) {
    await crawlab.saveItem({
      'hello': 'world'
    })
  }
  await crawlab.close()
})()
