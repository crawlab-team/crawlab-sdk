package utils

import (
	"crawlab_sdk/constants"
	"crawlab_sdk/database"
	"crawlab_sdk/entity"
	"github.com/apex/log"
	"github.com/globalsign/mgo"
	"github.com/globalsign/mgo/bson"
	"runtime/debug"
)

func SaveItem(item entity.Item) (err error) {
	dsType := GetDataSourceType()
	if dsType == constants.DataSourceTypeMongo {
		if err := SaveItemMongo(item); err != nil {
			log.Errorf("save item error: " + err.Error())
			debug.PrintStack()
			return err
		}
		return nil
	} else if dsType == constants.DataSourceTypeKafka {
		if err := SaveItemKafka(item); err != nil {

		}
	} else if dsType == constants.DataSourceTypeElasticSearch {
	}
	return nil
}

func SaveItemMongo(item entity.Item) (err error) {
	_, c, err := database.GetMongoCol()
	item["task_id"] = GetTaskId()

	isDedup := GetIsDedup()

	if isDedup == "1" {
		// 去重
		dedupField := GetDedupField()
		dedupMethod := GetDedupMethod()
		if dedupMethod == constants.DedupMethodOverwrite {
			// 覆盖
			var res interface{}
			if err := c.Find(bson.M{dedupField: item[dedupField]}).One(&res); err != nil {
				if err == mgo.ErrNotFound {
					// 不存在
					if err := c.Insert(item); err != nil {
						log.Errorf("save item error: " + err.Error())
						debug.PrintStack()
						return err
					}
					return nil
				} else {
					log.Errorf("find item error: " + err.Error())
					debug.PrintStack()
					return err
				}
			} else {
				// 已存在
				if err := c.Update(bson.M{dedupField: item[dedupField]}, item); err != nil {
					log.Errorf("update item error: " + err.Error())
					debug.PrintStack()
					return err
				}
				return nil
			}
		} else if dedupMethod == constants.DedupMethodIgnore {
			// 忽略
			if err := c.Insert(item); err != nil {
				log.Errorf("save item error: " + err.Error())
				debug.PrintStack()
				return err
			}
			return nil
		} else {
			// 其他
			if err := c.Insert(item); err != nil {
				log.Errorf("save item error: " + err.Error())
				debug.PrintStack()
				return err
			}
		}
	} else {
		// 不去重
		if err := c.Insert(item); err != nil {
			log.Errorf("save item error: " + err.Error())
			debug.PrintStack()
			return err
		}
		return nil
	}
	return nil
}

func SaveItemSql(item entity.Item) error {
	// TODO: implement SaveItemSql
	return nil
}

func SaveItemKafka(item entity.Item) error {
	// TODO: implement SaveItemKafka
	return nil
}

func SaveItemElasticSearch(item entity.Item) error {
	// TODO: implement SaveItemElasticSearch
	return nil
}
