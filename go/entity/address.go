package entity

import (
	"fmt"
)

type Address struct {
	Host string
	Port string
}

func (a *Address) String() (res string) {
	return fmt.Sprintf("%s:%s", a.Host, a.Port)
}

func (a *Address) IsEmpty() (res bool) {
	return a.Host == "" || a.Port == ""
}

func (a *Address) Value() (res interface{}) {
	return a
}

type AddressOptions struct {
	Host string
	Port string
}

func NewAddress(opts *AddressOptions) (res *Address) {
	if opts == nil {
		opts = &AddressOptions{}
	}
	if opts.Host == "" {
		opts.Host = "localhost"
	}
	if opts.Port == "" {
		opts.Port = "9666"
	}
	return &Address{
		Host: opts.Host,
		Port: opts.Port,
	}
}
