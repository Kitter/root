import os, json
from dvaclient import schema

if __name__ == '__main__':
    print "Starting validation"
    for root, directories, filenames in os.walk(os.path.join(os.path.dirname(__file__),'.')):
        print root, directories, filenames
        for filename in filenames:
            if filename.endswith('.json'):
                print "Validating {}".format(filename)
                validator = schema.Validator(json.load(file(os.path.join(root,filename))))
                validator.validate()