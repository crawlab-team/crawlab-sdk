const crawlab = require('../index');

(async () => {
  await crawlab.saveItem({
    'hello': 'world'
  })
  await crawlab.saveItem({
    'hello': 'world'
  })
  await crawlab.close()
})()
