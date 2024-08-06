import doctest
import math


def body_moving(H: float, v0: float, alpha: float, t: float) -> str:
    """
    Finds coordinates and the speed of the body at the time moment t, the maximum height and
    the maximum length of the trajectory of the body which is thrown from the height H with the speed v0 and
    the angle alpha

   :param H: float
   :param v0: float
   :param alpha: float
   :param t: float

    >>> body_moving(34.5, 10.0, 90.0, 0.0)
    Coordinates of the body at the time moment 0.0 are 0.0 and 34.5;
    the speed of the body at the time moment 0.0 is 10.0;
    the maximum height is 39.5;
    the maximum length is 0.0.
    >>> body_moving(-50, 10.0, 90.0, 0.0)
    Height H must be positive number
    >>> body_moving(50, -10.0, 90.0, 0.0)
    Speed v0 must be positive number
    >>> body_moving(-50, -10.0, 90.0, 0.0)
    Height H and speed v0 must be positive numbers
    >>> body_moving(50, 10.0, 90.0, -1.0)
    Time moment t must be positive number
    >>> body_moving(-50, -10.0, 90.0, -1.0)
    Height H, speed v0 and time moment must be positive numbers
    >>> body_moving(-50, 10.0, 90.0, -1.0)
    Height H and time moment must be positive numbers
    >>> body_moving(50, -10.0, 90.0, -1.0)
    Speed v0 and time moment must be positive numbers

    """

    if H < 0 and v0 < 0 and t < 0:
        print(f"Height H, speed v0 and time moment must be positive numbers")
    elif H < 0 and t < 0:
        print(f"Height H and time moment must be positive numbers")
    elif H < 0 and v0 < 0:
        print(f"Height H and speed v0 must be positive numbers")
    elif v0 < 0 and t < 0:
        print(f"Speed v0 and time moment must be positive numbers")
    elif H < 0:
        print(f"Height H must be positive number")
    elif v0 < 0:
        print(f"Speed v0 must be positive number")
    elif t < 0:
        print(f"Time moment t must be positive number")
    else:
        g = 10
        alpha_rad = alpha * math.pi / 180
        x = v0 * math.cos(alpha_rad) * t
        y = H + v0 * math.sin(alpha_rad) * t - (0.5 * g * t ** 2)
        Vx = v0 * math.cos(alpha_rad)
        Vy = v0 * math.sin(alpha_rad)
        V = math.sqrt(Vx ** 2 + Vy ** 2)
        max_height = H + (v0 ** 2 * math.sin(alpha_rad) ** 2) / (g * 2)
        max_lenght = (v0 ** 2 * math.sin(alpha_rad * 2)) / g

        print(f"Coordinates of the body at the time moment {t} are {round(x, 2)} and {round(y, 2)};\n" +
              f"the speed of the body at the time moment {t} is {round(V, 2)};\n" +
              f"the maximum height is {round(max_height, 2)};\n" +
              f"the maximum length is {round(max_lenght, 2)}.")

H = float(input("Input start height:"))
v0 = float(input("Input start speed:"))
alpha = float(input("Input alpha"))
t = float(input("Input time moment:"))
body_moving(H, v0, alpha, t)

doctest.testmod()
