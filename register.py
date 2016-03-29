# load json object
# instantiate the classes
# run their create / update commands.

from collector.core.dataset import Dataset



d = Dataset(dataset_object=metadata,
    base_url='http://data.hdx.rwlabs.org', apikey='test')

print(d._check())
