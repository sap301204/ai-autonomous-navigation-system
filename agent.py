class Agent:
    def __init__(self, start_position):
        self.position = start_position
        self.path_index = 0

    def move_along_path(self, path):
        """
        Move one step along the planned path
        """
        if not path:
            return False

        if self.path_index < len(path) - 1:
            self.path_index += 1
            self.position = path[self.path_index]
            return True

        return False

    def reset(self, start_position):
        """
        Reset agent position
        """
        self.position = start_position
        self.path_index = 0