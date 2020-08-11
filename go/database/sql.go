package database

import (
	"errors"
	"fmt"
	"github.com/apex/log"
	"github.com/crawlab-team/crawlab-sdk/go/constants"
	"github.com/crawlab-team/crawlab-sdk/go/entity"
	"github.com/crawlab-team/crawlab-sdk/go/utils"
	"github.com/jmoiron/sqlx"
	"runtime/debug"
	"strings"
)

var Db *sqlx.DB

func GetSqlDatabaseConnectionString(dataSourceType string, host string, port string, username string, password string, database string) (connStr string, err error) {
	// 获取数据库链接串
	if dataSourceType == constants.DataSourceTypeMysql {
		connStr = fmt.Sprintf("%s:%s@(%s:%s)/%s?charset=utf8&parseTime=True&loc=Local", username, password, host, port, database)
	} else if dataSourceType == constants.DataSourceTypePostgres {
		connStr = fmt.Sprintf("host=%s port=%s user=%s dbname=%s password=%s sslmode=%s", host, port, username, database, password, "disable")
	} else {
		err = errors.New(dataSourceType + " is not implemented")
		log.Errorf(err.Error())
		debug.PrintStack()
		return connStr, err
	}
	return connStr, nil
}

func GetSqlDatabase() *sqlx.DB {
	if Db != nil {
		return Db
	}

	ds := utils.GetDataSource()

	// 获取数据库链接串
	connStr, err := GetSqlDatabaseConnectionString(ds.Type, ds.Host, ds.Port, ds.Username, ds.Password, ds.Database)
	if err != nil {
		log.Errorf("get connection string error: " + err.Error())
		debug.PrintStack()
		return Db
	}

	// 数据库
	Db, err = sqlx.Open(ds.Type, connStr)
	if err != nil {
		log.Errorf("open database error: " + err.Error())
		debug.PrintStack()
	}

	return Db
}

func InsertItem(item entity.Item) (err error) {
	db := GetSqlDatabase()
	col := utils.GetCollection()
	if _, err := db.Exec(fmt.Sprintf("INSERT INTO %s (%s) VALUES (%s)",
		col,
		strings.Join(utils.GetItemKeys(item), ","),
		strings.Join(utils.GetItemValuesWithQuote(item), ","),
	)); err != nil {
		log.Errorf("insert item error: " + err.Error())
		debug.PrintStack()
		return err
	}
	return nil
}

func UpdateItem(item entity.Item, dedupField string) (err error) {
	db := GetSqlDatabase()
	col := utils.GetCollection()
	if _, err := db.Exec(fmt.Sprintf("UPDATE %s SET %s WHERE %s = '%s'",
		col,
		utils.GetItemSqlUpdateStr(item),
		dedupField,
		item[dedupField],
	)); err != nil {
		log.Errorf("update item error: " + err.Error())
		debug.PrintStack()
		return err
	}
	return nil
}

func GetItem(key string, value string) (item entity.Item, err error) {
	db := GetSqlDatabase()
	col := utils.GetCollection()
	if err := db.QueryRow(fmt.Sprintf("SELECT * FROM %s WHERE %s = '%s'",
		col,
		key,
		value,
	)).Scan(&item); err != nil {
		log.Errorf("update item error: " + err.Error())
		debug.PrintStack()
		return item, err
	}
	return item, nil
}
