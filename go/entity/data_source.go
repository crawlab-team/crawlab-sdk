package entity

import (
	"github.com/globalsign/mgo/bson"
	"time"
)

type DataSource struct {
	Id         bson.ObjectId `json:"_id" bson:"_id"`
	Type       string        `json:"type" bson:"type"`
	Host       string        `json:"host" bson:"host"`
	Port       string        `json:"port" bson:"port"`
	Database   string        `json:"database" bson:"database"`
	Username   string        `json:"username" bson:"username"`
	Password   string        `json:"password" bson:"password"`
	AuthSource string        `json:"auth_source" bson:"auth_source"`
	UserId     bson.ObjectId `json:"user_id" bson:"user_id"`
	CreateTs   time.Time     `json:"create_ts" bson:"create_ts"`
	UpdateTs   time.Time     `json:"update_ts" bson:"update_ts"`
}
