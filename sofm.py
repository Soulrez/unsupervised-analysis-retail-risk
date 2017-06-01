import numpy as np
from matplotlib import pyplot as plt
from sompy.sompy import SOMFactory
from sklearn.datasets import fetch_california_housing

np.set_printoptions(threshold=np.nan)

# FULL DATA
with open('data/safeway/'+"report.csv") as f:
	# Convert formatted data to numpy Array
	data = np.asarray([map(float, i.split(',')) for i in f])

# FULL FEATURES
names = ["Risk Factor",
		"Total Number Of Transactions",
		"Total Items Count",
		"Total Sales Amount",
		"Coupons outside of orders",
		"Coupons Highest # Promo Code Use",
		"Coupons % Of Total Amount",
		"Coupons Total Amount",
		"Coupons Count",
		"Coupons Average Amount",
		"Coupons % Of All Trx",
		"Refunds Trx Count",
		"Refunds Item Count",
		"Refunds Total Amount",
		"Dept Refunds % Of Total Amount",
		"Dept Refunds Total Amount	",
		"Dept Refunds % Of Items	",
		"Dept Refunds Item Count",
		"Item Voids Item Count",
		"Item Voids Total Amount",
		"Dept Sales % Of All Items",
		"Dept Sales Item Count",
		"Dept Sales Total Amount",
		"Zero Trx Percentage",
		"Zero Count",
		"Zero Trx With Alcohol",
		"Max No Of Card Uses",
		"No. Sales Per Day",
		"Base Avg Basket Size"]

#msz = calculate_msz(data)
# Neuron grid-size
msz0 = 100
msz1 = 100

# Training process
sm = SOMFactory().build(data, normalization = 'var', initialization='random', component_names=names, mapsize=[msz0,msz1])
sm.train(n_job=1, verbose=False, train_rough_len=2, train_finetune_len=5)

# Calculate loss
topographic_error = sm.calculate_topographic_error()
quantization_error = np.mean(sm._bmu[1])
print "Topographic error = %s; Quantization error = %s" % (topographic_error, quantization_error)

# 2D graph visualization
from sompy.visualization.mapview import View2D
view2D  = View2D(150,150,"rand data",text_size=10)
view2D.show(sm, col_sz=5, desnormalize=True)

'''
# K-means clustering of data for comparison
from sompy.visualization.hitmap import HitMapView
sm.cluster(4)
hits  = HitMapView(150,150,"Clustering",text_size=12)
a=hits.show(sm)
'''