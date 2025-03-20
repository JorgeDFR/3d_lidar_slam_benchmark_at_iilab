#!/bin/bash
set -e

# setup ros1 environment
source "/opt/ros/noetic/setup.bash" --
exec "$@"