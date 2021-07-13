# please install facet-overview

from sklearn.datasets import load_iris
from IPython.core.display import display, HTML
import numpy as np
import pandas as pd

my_iris = load_iris()
x = my_iris.data
y = my_iris.target

iris_data = np.c_[x,y]

iris_columns = ['sepal length (cm)',
  'sepal width (cm)',
  'petal length (cm)',
  'petal width (cm)']
header=iris_columns+['iris_class']

iris_df = pd.DataFrame(data=iris_data, columns = header)

# Giving each class a meaningful name e.g. class 1 = Setosa
iris_df['iris_class'].replace(0.0, 'Setosa', inplace=True)
iris_df['iris_class'].replace(1.0, 'Versicolor', inplace=True)
iris_df['iris_class'].replace(2.0, 'Virginica', inplace=True)

jsonstr = iris_df.to_json(orient='records')
HTML_TEMPLATE = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>
<link rel="import" href="https://raw.githubusercontent.com/PAIR-code/facets/1.0.0/facets-dist/facets-jupyter.html">
<facets-dive id="elem" height="600"></facets-dive>
<script>
var data = {jsonstr};
document.querySelector("#elem").data = data;
</script>"""
html = HTML_TEMPLATE.format(jsonstr=jsonstr)
display(HTML(html))

