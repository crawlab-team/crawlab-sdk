package database

import (
	"context"
	"fmt"
	"github.com/apex/log"
	"github.com/crawlab-team/crawlab-sdk/go/entity"
	"github.com/crawlab-team/crawlab-sdk/go/utils"
	"github.com/olivere/elastic/v7"
	"runtime/debug"
)

func GetElasticSearchClient() (client *elastic.Client, err error) {
	ds := utils.GetDataSource()
	if ds.Username != "" {
		client, err = elastic.NewClient(
			elastic.SetURL(fmt.Sprintf("http://%s:%s", ds.Host, ds.Port)),
			elastic.SetBasicAuth(ds.Username, ds.Password),
			elastic.SetHealthcheck(false),
			elastic.SetSniff(false),
		)
	} else {
		client, err = elastic.NewClient(
			elastic.SetURL(fmt.Sprintf("http://%s:%s", ds.Host, ds.Port)),
			elastic.SetHealthcheck(false),
			elastic.SetSniff(false),
		)
	}
	if err != nil {
		log.Error("new client error: " + err.Error())
		debug.PrintStack()
		return client, err
	}
	return client, nil
}

func IndexItem(item entity.Item) (err error) {
	ds := utils.GetDataSource()
	client, err := GetElasticSearchClient()
	if err != nil {
		return err
	}
	_, err = client.Index().
		Index(ds.Database).
		BodyJson(item).
		Refresh("true").
		Do(context.TODO())
	if err != nil {
		log.Errorf("index item error: " + err.Error())
		debug.PrintStack()
		return err
	}
	return nil
}
