import json
import config

class JSONModel(object):

    def __init__(self, directory):
        self.load_data(directory)

    def all(self):
        pass

    def exists(self, id):
        pass

    def get(self, id):
        pass

    def load_data(self, directory):
        self.data = json.load(open(directory))


class Character(JSONModel):

    def __init__(self, directory=config.DATA_CHARACTERS_FILE_DIR):
        super().__init__(directory)

    def all(self):
        return self.data

    def get(self, id):
        character_index = self.get_ids().index(id)
        return self.data[character_index]

    def exists(self, id):
        return id in self.get_ids()

    def get_ids(self):
        return [character['_id'] for character in self.data]
