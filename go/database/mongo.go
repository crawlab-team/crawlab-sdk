package database

import (
	"crawlab_sdk/utils"
	"github.com/apex/log"
	"github.com/globalsign/mgo"
	"net"
	"os"
	"runtime/debug"
	"time"
)

var Session *mgo.Session

func GetDataSourceCol(host string, port string, username string, password string, authSource string, database string, col string) (*mgo.Session, *mgo.Collection, error) {
	timeout := time.Second * 10
	dialInfo := mgo.DialInfo{
		Addrs:         []string{net.JoinHostPort(host, port)},
		Timeout:       timeout,
		Database:      database,
		PoolLimit:     100,
		PoolTimeout:   timeout,
		ReadTimeout:   timeout,
		WriteTimeout:  timeout,
		AppName:       "crawlab",
		FailFast:      true,
		MinPoolSize:   10,
		MaxIdleTimeMS: 1000 * 30,
	}
	if username != "" {
		dialInfo.Username = username
		dialInfo.Password = password
		dialInfo.Source = authSource
	}
	if Session == nil {
		s, err := mgo.DialWithInfo(&dialInfo)
		if err != nil {
			log.Errorf("dial mongo error: " + err.Error())
			debug.PrintStack()
			return nil, nil, err
		}
		Session = s
	}
	db := Session.DB(database)
	return Session, db.C(col), nil
}

func GetMongoCol() (*mgo.Session, *mgo.Collection, error) {
	ds := utils.GetDataSource()
	if ds.Type == "" {
		return GetDataSourceCol(
			os.Getenv("CRAWLAB_MONGO_HOST"),
			os.Getenv("CRAWLAB_MONGO_PORT"),
			os.Getenv("CRAWLAB_MONGO_USERNAME"),
			os.Getenv("CRAWLAB_MONGO_PASSWORD"),
			os.Getenv("CRAWLAB_MONGO_AUTHSOURCE"),
			os.Getenv("CRAWLAB_MONGO_DATABASE"),
			utils.GetCollection(),
		)
	}
	return GetDataSourceCol(
		ds.Host,
		ds.Port,
		ds.Username,
		ds.Password,
		ds.AuthSource,
		ds.Database,
		utils.GetCollection(),
	)
}
