package database

import (
	"encoding/json"
	"fmt"
	"github.com/apex/log"
	"github.com/crawlab-team/crawlab-sdk/go/entity"
	"github.com/crawlab-team/crawlab-sdk/go/utils"
	"github.com/segmentio/kafka-go"
	"runtime/debug"
)

func GetKafkaConnection() (conn *kafka.Conn, err error) {
	ds := utils.GetDataSource()
	conn, err = kafka.Dial(
		"tcp",
		fmt.Sprintf("%s:%s", ds.Host, ds.Port),
	)
	if err != nil {
		log.Errorf("dial kafka error: " + err.Error())
		debug.PrintStack()
		return conn, err
	}
	return conn, nil
}

func SendKafkaMsg(item entity.Item) (err error) {
	ds := utils.GetDataSource()
	conn, err := GetKafkaConnection()
	if err != nil {
		return err
	}
	msgStr, err := json.Marshal(&item)
	if err != nil {
		log.Errorf("marshal json error: " + err.Error())
		debug.PrintStack()
		return err
	}
	if _, err := conn.WriteMessages(
		kafka.Message{
			Topic:     ds.Database,
			Partition: 0,
			Value:     msgStr,
		},
	); err != nil {
		log.Errorf("send kafka message error: " + err.Error())
		debug.PrintStack()
		return err
	}
	return nil
}
