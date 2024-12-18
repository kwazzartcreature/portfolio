package main

import (
	"api/internal/config"
	"log"
	"os"

	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
)

func main() {
    config.InitLogger() 
    app := pocketbase.New()

    app.OnServe().BindFunc(func(se *core.ServeEvent) error {
        se.Router.GET("/{path...}", apis.Static(os.DirFS("./pb_public"), false))
        return se.Next()
    })

    if err := app.Start(); err != nil {
        log.Fatal(err)
    }
}