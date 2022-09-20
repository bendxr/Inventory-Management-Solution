class NonExistentItemException(KeyError):
  def __init__(self, message):
    """
    :param message: specific message of the exception
    """
    self.message = message