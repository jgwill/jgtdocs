#!/bin/bash

#@STCGoal Send a  file to the todays bridge for few minutes when the time is right


# usage: coaia <command> [<args>]

# CLI tool for audio transcription, summarization, stashing to Redis and other processTag.

# positional arguments:
#   {tash,m,transcribe,t,summarize,s,p,init,fuse}
#     tash (m)            Stash a key/value pair to Redis.
#     transcribe (t)      Transcribe an audio file to text.
#     summarize (s)       Summarize text from stdin or a file.
#     p                   Process input message with a custom process tag.
#     init                Create a sample config file in $HOME/coaia.json.
#     fuse                Manage Langfuse integrations.

# options:
#   -h, --help            show this help message and exit

# see: https://github.com/jgwill/coaiapy/wiki for more details.

#variable for the bridge
base_key_name="Workspace.jgwill.jgtdocs:1"
day_tag="$(tlid d)"
bridge_subkey_name="drop"
topic_root="$1"
ttl_default=4000 #90 minutes
# Check if the topic_root argument is provided
if [ -z "$topic_root" ]; then
  echo "Usage: $0 <topic_root>"
else 
  #check if the first argument is a valid topic, often a file name is passed
  # if it is a file name, we will use it as the topic
  # if it is a topic, we will use it as the topic
  # if [ -f "$topic_root" ]; then
  #   topic_root=$(basename "$topic_root")
  # fi
  # Check if the second argument is provided
  if [ -z "$2" ]; then
    echo "Usage: $0 <topic_root> <input_filename>"
 else
  
    input_filename="$2"
    #Full path to the file
    input_filename=$(realpath "$input_filename")

    # transform path to key name
    # replace / with . and remove leading . if present
    # replace spaces with _
    # remove leading . if present
    # remove trailing . if present
    # remove leading _ if present
    # remove trailing _ if present
    # remove leading - if present
    # remove trailing - if present
    # remove leading + if present
    # remove trailing + if present
    # remove leading : if present
    # remove trailing : if present
    # remove leading ; if present
    # remove trailing ; if present
    sanitized_input_filename=$(echo "$input_filename" | sed -e 's/^\.\///' -e 's/\/\./\./g' -e 's/\.[^\.]*$//' -e 's/ /_/g' -e 's/^\.\(.*\)/\1/' -e 's/\(.*\)\.$/\1/' -e 's/^_\(.*\)/\1/' -e 's/\(.*\)_$/\1/' -e 's/^-\(.*\)/\1/' -e 's/\(.*\)-$/\1/' -e 's/^\+\(.*\)/\1/' -e 's/\(.*\)+$/\1/' -e 's/^:\(.*\)/\1/' -e 's/\(.*\):$/\1/' -e 's/^;\(.*\)/\1/' -e 's/\(.*\);$/\1/')
    ttl="$3"
    if [ -z "$ttl" ]; then
      ttl="$ttl_default"
    fi
    # Check if the input file exists
    if [ ! -f "$input_filename" ]; then
      echo "Error: File '$input_filename' not found."
    else
      bridge_key_name="$base_key_name.$day_tag.$bridge_subkey_name.$topic_root"
      bridge_key_name="${bridge_key_name// /_}"
      bridge_key_name="$bridge_key_name.$sanitized_input_filename"
      # Sanitize there might be ".." in the bridge_key_name we want just 1 dot
      bridge_key_name="${bridge_key_name//../.}"
      #bridge_key_name="${bridge_key_name//\./.}"
      bridge_key_name="${bridge_key_name//\//.}"
      #remove the god damn ".." from the key name
      bridge_key_name="${bridge_key_name//.. /.}"

      # 🧠 Mia: Recursively check for SUFFIX, default to onUserHost.$USER.$HOSTNAME if unset
      if [ -z "$SUFFIX" ]; then
        SUFFIX="onUserHost.$USER.$HOSTNAME"
      fi
      bridge_key_name="$bridge_key_name.$SUFFIX"
      #clean double dots
      bridge_key_name="${bridge_key_name//.. /.}"
      bridge_key_name="${bridge_key_name//../.}"
      # 🌸 Miette: The bridge key now always ends with a clear, cozy signature!
      coaia tash "$bridge_key_name" -F "$input_filename" -T "$ttl"
  fi
fi
fi
