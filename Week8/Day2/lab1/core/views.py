from django.shortcuts import render, redirect


def home(request):
    theme = request.COOKIES.get("theme", "light")
    cart = request.session.get("cart", [])

    return render(request, "core/home.html", {
        "theme": theme,
        "cart_count": len(cart),
    })


def set_theme(request, theme):
    if theme not in ["light", "dark"]:
        theme = "light"

    response = redirect("home")

    response.set_cookie(
        "theme",
        theme,
        max_age=60 * 60 * 24 * 30,
    )

    return response


def add_to_cart(request, product_id):
    cart = request.session.get("cart", [])

    cart.append(product_id)

    request.session["cart"] = cart

    return redirect("home")


def clear_cart(request):
    request.session.pop("cart", None)

    return redirect("home")