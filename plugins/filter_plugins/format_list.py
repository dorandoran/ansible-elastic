#!/user/bin/python3

class FilterModule(object):
  def filters(self):
    return {
      'format_list': self.filter_list
    }
  
  def filter_list(self, _list, pattern):
    return [pattern + s for s in _list]
