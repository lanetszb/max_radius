def implement_bool_shooting_method(bool_function, init_x, init_dx, min_dx):
    x = init_x
    dx = init_dx
    y_curr = bool_function(x)
    y_prev = y_curr
    while True:
        x += dx
        y_prev = y_curr
        y_curr = bool_function(x)
        if y_curr != y_prev:
            dx /= -2.
        if abs(dx) < min_dx:
            break
    return x, dx

