package interfaces

import "github.com/crawlab-team/crawlab-go-sdk/entity"

type ResultService interface {
	SaveItem(item ...entity.Result)
	SaveItems(item []entity.Result)
}
