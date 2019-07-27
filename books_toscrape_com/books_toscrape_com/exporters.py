import csv

from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter


class CsvExtendedItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        settings = get_project_settings()
        dialect = settings.get('CSV_DIALECT')
        kwargs['dialect'] = csv.get_dialect('dialect') if dialect in csv.list_dialects() else csv.get_dialect('excel')
        kwargs['delimiter'] = settings.get('CSV_DELIMITER', kwargs['dialect'].delimiter)
        kwargs['doublequote'] = settings.get('CSV_DOUBLEQUOTE', kwargs['dialect'].doublequote)
        kwargs['escapechar'] = settings.get('CSV_ESCAPECHAR', kwargs['dialect'].escapechar)
        kwargs['lineterminator'] = settings.get('CSV_LINETERMINATOR', kwargs['dialect'].lineterminator)
        kwargs['quotechar'] = settings.get('CSV_QUOTECHAR', kwargs['dialect'].quotechar)
        kwargs['quoting'] = settings.get('CSV_QUOTING', kwargs['dialect'].quoting)
        super(CsvExtendedItemExporter, self).__init__(*args, **kwargs)
