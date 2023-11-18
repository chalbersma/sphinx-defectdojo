from collections import defaultdict


from docutils.parsers.rst import directives, Directive
from docutils.parsers.rst.directives.tables import ListTable
from docutils import nodes, utils, frontend
from docutils.utils import SystemMessagePropagation, Reporter

import sphinx
from sphinx.util import logging
from sphinx.application import Sphinx


class DojoFinding(ListTable):
    """
    Example of the directive:

    .. code-block:: rest

      .. dojofinding::
         :finding: 20

      .. dojofinding::
         :test: 20
         
      .. dojofinding::
         :productname: somename

    """


    has_content = False


    option_spec = {

        'finding': directives.nonnegative_int,
        'test': directives.nonnegative_int,
        'productname': directives
    }


    def run(self):
        """
        Implements the directive
        """
        # Get content and options
        findings = self.options.get('finding', None)
        test = self.options.get('test', None)
        productname = self.options.get('productname', None)

        header_rows = 1
        stub_columns = 0

        '''
        # Dynamic Col Widths in the Future
        if col_widths:
            col_widths = [int(width) for width in col_widths.split(',')]
        else:
            col_widths = [int(col['width']) for col in table['rows'][0]]
            col_width_total = sum(col_widths)
            col_widths = [int(width * 100 / col_width_total) for width in col_widths]
        '''


        if findings is None and test is None and productname is None:
            return [self._report(u"No Finding, test or productname given")]


        table_data = []

        table_data.append([nodes.paragraph(text="Header 1"), nodes.paragraph(text="Header 2")])
        table_data.append([nodes.paragraph(text="Value 1"), nodes.paragraph(text="Value 2")])

        table_node = self.build_table_from_list(table_data, col_widths=[50,50], header_rows=1, stub_columns=0)

        print(table_node)


        return [table_node]

