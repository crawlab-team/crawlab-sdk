package sdk

import (
	"context"
	"encoding/json"
	grpc "github.com/crawlab-team/crawlab-grpc"
	"github.com/crawlab-team/crawlab-sdk/entity"
	"github.com/crawlab-team/crawlab-sdk/interfaces"
	"github.com/crawlab-team/go-trace"
)

var RS = NewResultService()

type ResultService struct {
	// internals
	sub grpc.TaskService_SubscribeClient
}

func (svc *ResultService) SaveItem(items ...entity.Result) {
	svc.save(items)
}

func (svc *ResultService) SaveItems(items []entity.Result) {
	svc.save(items)
}

func (svc *ResultService) save(items []entity.Result) {
	// skip if no task id specified
	if GetTaskId().IsZero() {
		return
	}

	var records []interface{}
	for _, item := range items {
		records = append(records, item)
	}
	data, err := json.Marshal(&entity.StreamMessageTaskData{
		TaskId:  GetTaskId(),
		Records: records,
	})
	if err != nil {
		trace.PrintError(err)
		return
	}
	if err := svc.sub.Send(&grpc.StreamMessage{
		Code: grpc.StreamMessageCode_INSERT_DATA,
		Data: data,
	}); err != nil {
		trace.PrintError(err)
		return
	}
}

func (svc *ResultService) init() (err error) {
	svc.sub, err = C.GetTaskClient().Subscribe(context.Background())
	if err != nil {
		return trace.TraceError(err)
	}
	return nil
}

func NewResultService(opts ...ResultServiceOption) interfaces.ResultService {
	// service
	svc := &ResultService{}

	// apply options
	for _, opt := range opts {
		opt(svc)
	}

	// initialize
	if err := svc.init(); err != nil {
		panic(err)
	}

	return svc
}

func SaveItem(items ...entity.Result) {
	RS.SaveItem(items...)
}

func SaveItems(items []entity.Result) {
	RS.SaveItems(items)
}
