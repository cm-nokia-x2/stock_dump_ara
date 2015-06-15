#!/bin/sh

function test {
    "$@"
    status=$?
    if [ $status -ne 0 ]; then
        echo "error with $1"
    fi
    return $status
}

test camera_pt_app $1

