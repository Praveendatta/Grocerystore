from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='count')
def count(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * count(product, cart)


@register.filter(name='total_cart')
def total_cart(products, cart):
    ans = 0
    for p in products:
        ans += price_total(p, cart)
    return ans


@register.filter(name='total_100')
def total_100(products, cart):
    ans = 10 + total_cart(products, cart)
    return ans


@register.filter(name='coupon')



@register.filter(name='cvalue')



@register.filter(name='ctotal')
def ctotal(ptotal, dvalue):
    return ptotal - (ptotal * dvalue) / 100
