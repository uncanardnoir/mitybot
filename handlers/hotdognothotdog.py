import urllib
import ImageFile
import tensorflow as tf
import sys
import os
import requests

def getsize(uri):
  try:
    file = urllib.urlopen(uri)
    return int(file.headers.get("content-length"))
  except:
    return -1

class HotdogNotHotdog:
  def __init__(self):
    with tf.gfile.FastGFile("hot_dog_graph.pb", 'rb') as inception_graph:
      os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
      definition = tf.GraphDef()
      definition.ParseFromString(inception_graph.read())
      _ = tf.import_graph_def(definition, name='')

  def handleCommand(self, command):
    if not command.args:
      return None
    url = command.args
    ispng = False
    isjpg = False
    if url.endswith("png"):
      ispng = True
    if url.endswith("jpg") or url.endswith("jpeg"):
      isjpg = True
    if not ispng and not isjpg:
      return "File must be png or jpg"
    ret = getsize(url)
    if ret == -1:
      return "Failed to download file"
    if ret > 1048576:
      return "File over limit of 1 mb"
    r = requests.get(url, stream=True)
    filename = 'hotdog.png' if ispng else 'hotdog.jpg'
    with open(filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=1024):
        if chunk:
          f.write(chunk)
    image_file = tf.gfile.FastGFile(filename, 'rb')
    data = image_file.read()
 
    with tf.Session() as session:
      try:
        tensor = session.graph.get_tensor_by_name('final_result:0')
        result = session.run(tensor, {'DecodeJpeg/contents:0': data})
        top_results = result[0].argsort()[-len(result[0]):][::-1]
        for type in top_results:
          hotdogprob = result[0][0]
          if hotdogprob > 0.5:
            return "Is.. HOT DOG! (hot dog prob: {0})".format(hotdogprob)
          else:
            return "Is.. NOT HOT DOG! (hot dog prob: {0})".format(hotdogprob)
      except:
        return "An error occurred"
