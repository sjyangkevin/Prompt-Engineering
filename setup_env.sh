#!/bin/bash
export PROJECT_DIR=$(pwd)
export $(cat .env | xargs)
