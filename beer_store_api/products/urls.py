from django.conf.urls import patterns, url
from products import views

urlpatterns = patterns("",
	# /stores
	url(
		regex=r"^stores/$",
		view=views.stores,
		name="beer_store_api"
	),

	# /stores/{store_id}
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/$",
		view=views.store_by_id,
		name="beer_store_api"
	),

	# /products
	url(
		regex=r"^products/$",
		view=views.products,
		name="beer_store_api"
	),

	# /products/{product_id}
	url(
		regex=r"^products/(?P<product_id>[0-9]+)/$",
		view=views.product_by_id,
		name="beer_store_api"
	),

	# /stores/{store_id}/products
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/products/$",
		view=views.products_at_store,
		name="beer_store_api"
	),

	# /products/{product_id}/stores
	url(
		regex=r"^products/(?P<product_id>[0-9]+)/stores/$",
		view=views.stores_with_product,
		name="beer_store_api"
	),

	# /stores/{store_id}/products/{product_id}/inventory
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/products/(?P<product_id>[0-9]+)/inventory/$",
		view=views.inventory,
		name="beer_store_api"
	),
)