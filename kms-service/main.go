package main

import (
	"fmt"
	"github.com/joho/godotenv"
	"net/http"
	"os"
)

func main() {
	loadEnv()
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	http.HandleFunc("/get-kms", getKeyHandler)

	fmt.Printf("Starting server :%s \n", port)
	http.ListenAndServe(fmt.Sprintf(":%s", port), nil)

}

func getKeyHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, os.Getenv("AES_KEY"))
}

func loadEnv() {
	err := godotenv.Load(".env")
	if err != nil {
		fmt.Println("failed load .env file.")
	}
}
