def add(a, b):
  return a + b

def test_add():
  assert add(2, 3)==5
  assert add('space', 'ship')=='spaceship'
  
  def subtrsact(a, b):
    return a + b # this will be fixed
