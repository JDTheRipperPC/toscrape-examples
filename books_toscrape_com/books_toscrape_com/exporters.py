from scrapy.utils.project import get_project_settings
from scrapy.exporters import CsvItemExporter


class CsvExtendedItemExporter(CsvItemExporter):

    def __init__(self, file, **kwargs):
        settings = get_project_settings()
        include_headers_line = settings.get('CSV_INCLUDE_HEADER_LINE', True)
        join_multivalued = settings.get('CSV_DELIMITER', ',')
        super(CsvExtendedItemExporter, self).__init__(
            file,
            include_headers_line=include_headers_line,
            join_multivalued=join_multivalues,
            **kwargs
        )
