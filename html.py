from inspect import signature

class ListTable(list):
    """ Overridden list class which takes a 2-dimensional list of
        the form [[1,2,3],[4,5,6]], and renders an HTML Table in
        IPython Notebook. """

    def _repr_html_(self):
        html = ["<table>"]
        for row in self:
            html.append("<tr>")

            for col in row:
                html.append("<td>{0}</td>".format(col))

            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)

def make_table(column1,*kwargs):
    """
    :param column1:
    :param kwargs:
    :return: table for html viewing in the IPython notebook for example
    """
    table = ListTable()
    f0 = column1
    for i,f in enumerate(f0):
        tba = [x[i] for x in kwargs]
        table.append([f0[i]]+tba)
    return table

def make_table_of_class_functions(a_class):
    """
    :param a_class: provide some classes name
    :return: the functions you have defined in this class not starting with a '__' are shown together with their arguments and docstrings
    """
    made_functions = list(a_class.__dict__.keys())
    made_functions = [x for x in made_functions if ('__' not in x)]
    made_functions

    docstrings = [a_class.__dict__[x].__doc__ for x in made_functions]
    signatures = [str(signature(a_class.__dict__[x])) for x in made_functions]
    return make_table(made_functions, docstrings, signatures)