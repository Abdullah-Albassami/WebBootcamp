from django.shortcuts import render
from django.core.paginator import Paginator
# from django.http import Http404

from .data import products



def product_list(request):

    # Make a copy so the original mock data is not changed.
    filtered_products = products.copy()

    # -------------------------
    # GET query parameters
    # -------------------------

    category = request.GET.get("category")
    min_price = request.GET.get("min_price")
    q = request.GET.get("q", "")
    sort = request.GET.get("sort", "name")

    # -------------------------
    # CATEGORY FILTER
    # -------------------------

    if category:
        filtered_products = [
            product
            for product in filtered_products
            if product["category"].lower() == category.lower()
        ]

    # -------------------------
    # MINIMUM PRICE FILTER
    # -------------------------

    if min_price:

        try:
            min_price = float(min_price)

            filtered_products = [
                product
                for product in filtered_products
                if product["price"] >= min_price
            ]

        except ValueError:
            # Invalid min_price is ignored.
            min_price = ""

    # -------------------------
    # SEARCH
    # -------------------------

    if q:
        filtered_products = [
            product
            for product in filtered_products
            if q.lower() in product["name"].lower()
        ]

    # -------------------------
    # SORTING
    # -------------------------

    allowed_sorts = ["name", "price", "rating"]

    if sort not in allowed_sorts:
        sort = "name"

    filtered_products = sorted(
        filtered_products,
        key=lambda product: product[sort],
    )

    # -------------------------
    # PAGINATION
    # -------------------------

    paginator = Paginator(filtered_products, 3)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "category": category or "",
        "min_price": min_price or "",
        "q": q,
        "sort": sort,
    }

    return render(
        request,
        "products/product_list.html",
        context,
    )


def product_detail(request, id):

    # Find the product with the requested ID.
    product = next(
        (
            product
            for product in products
            if product["id"] == id
        ),
        None,
    )

    # Invalid product ID -> 404.
    if product is None:
        from django.http import Http404

        raise Http404("Product not found")

    # -------------------------
    # TAB QUERY PARAMETER
    # -------------------------

    tab = request.GET.get("tab", "details")

    allowed_tabs = [
        "details",
        "reviews",
        "shipping",
    ]

    # Invalid tab falls back to details.
    if tab not in allowed_tabs:
        tab = "details"

    context = {
        "product": product,
        "tab": tab,
    }

    return render(
        request,
        "products/product_detail.html",
        context,
    )