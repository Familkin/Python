{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Семинар 11. Jupyter Notebook и несколько слов об аналитике"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### f(x) = -12x^4*sin(cos(x)) - 18x^3 + 5x^2 + 10x - 30"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "1. Определить корни"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 6,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "'-48.7256484817221 -45.5199370667845 -42.4470735375890 -39.2313985972732 -36.1701099588650 -32.9407957980140 -29.8957796720679 -26.6466461586162 -23.6261972964361 -20.3455941359425 -17.3665525069077 -14.0280559916623 -11.1337690610358 -7.65062228513275 -5.02686592820621 -1.33896663927711 2.27305684575625 4.38352369796896 8.03516413341352 10.8606499895942 14.2405848102516 17.1928480700451 20.4926000632169 23.4988388764551 26.7590297922122 29.7952429281633 33.0317612356933 36.0870621935254 39.3078043212952 42.3763314152199 45.5858013946050 48.6640356793606 49.1396400840685 51.8650474071078'"
                        ]
                    },
                    "execution_count": 6,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "from decimal import Decimal, getcontext\n",
                "from sympy import *\n",
                "getcontext().prec = 20\n",
                "# from sympy.abc import x\n",
                "x = Symbol(\"x\")\n",
                "f = Function('f')\n",
                "# Корней бесконечное количество, поэтому ограничим промежуток от -50 до 50\n",
                "f = collect((-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30), x)\n",
                "roots = sorted(list([Decimal(str(r)) for r in {nsolve(f, x, i, prec=15, verify=False) for i in range(-50, 51)}]))\n",
                "' '.join([str(root) for root in roots])"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "2. Найти интервалы, на которых функция возрастает"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 7,
            "metadata": {},
            "outputs": [],
            "source": [
                "def fun(subx):\n",
                "    return f.subs(x, subx)\n",
                "\n",
                "def decimal_range(x, y, jump):\n",
                "  while x < y:\n",
                "    yield x\n",
                "    x += Decimal(jump)\n",
                "\n",
                "extremums = []\n",
                "f_positive_ranges = []\n",
                "f_negative_ranges = []\n",
                "\n",
                "for i in range(len(roots)-1):\n",
                "    points = [{'x': x, 'f': fun(x)} for x in decimal_range(roots[i], roots[i+1], '0.1')]\n",
                "\n",
                "    fs = [p['f'] for p in points]\n",
                "\n",
                "    if fs[len(fs)//2] > 0:\n",
                "        extremums.append([p for p in points if p['f'] == max(fs)][0])\n",
                "        f_positive_ranges.append((roots[i], roots[i+1]))\n",
                "    else:\n",
                "        extremums.append([p for p in points if p['f'] == min(fs)][0])\n",
                "        f_negative_ranges.append((roots[i], roots[i+1]))\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 8,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "Функция возрастает на интервалах Х:\n",
                        "-44.1199370667845 -> -40.9470735375890\n",
                        "-37.8313985972732 -> -34.7701099588650\n",
                        "-31.6407957980140 -> -28.4957796720679\n",
                        "-25.3466461586162 -> -22.2261972964361\n",
                        "-19.1455941359425 -> -16.0665525069077\n",
                        "-12.9280559916623 -> -9.9337690610358\n",
                        "-6.85062228513275 -> -4.12686592820621\n",
                        "1.66103336072289 -> 3.77305684575625\n",
                        "6.98352369796896 -> 9.83516413341352\n",
                        "13.0606499895942 -> 16.0405848102516\n",
                        "19.1928480700451 -> 22.1926000632169\n",
                        "25.3988388764551 -> 28.4590297922122\n",
                        "31.5952429281633 -> 34.7317612356933\n",
                        "37.8870621935254 -> 41.0078043212952\n",
                        "44.0763314152199 -> 47.2858013946050\n",
                        "49.0640356793606 -> 50.4396400840685\n"
                    ]
                }
            ],
            "source": [
                "print('Функция возрастает на интервалах Х:')\n",
                "for i in range(len(extremums)-1):\n",
                "    if (extremums[i]['f'])<0:\n",
                "        print(f'{extremums[i][\"x\"]} -> {extremums[i+1][\"x\"]}')\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "3. Найти интервалы, на которых функция убывает"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "Функция убывает на интервалах Х:\n",
                        "-47.2256484817221 -> -44.1199370667845\n",
                        "-40.9470735375890 -> -37.8313985972732\n",
                        "-34.7701099588650 -> -31.6407957980140\n",
                        "-28.4957796720679 -> -25.3466461586162\n",
                        "-22.2261972964361 -> -19.1455941359425\n",
                        "-16.0665525069077 -> -12.9280559916623\n",
                        "-9.9337690610358 -> -6.85062228513275\n",
                        "-4.12686592820621 -> 1.66103336072289\n",
                        "3.77305684575625 -> 6.98352369796896\n",
                        "9.83516413341352 -> 13.0606499895942\n",
                        "16.0405848102516 -> 19.1928480700451\n",
                        "22.1926000632169 -> 25.3988388764551\n",
                        "28.4590297922122 -> 31.5952429281633\n",
                        "34.7317612356933 -> 37.8870621935254\n",
                        "41.0078043212952 -> 44.0763314152199\n",
                        "47.2858013946050 -> 49.0640356793606\n"
                    ]
                }
            ],
            "source": [
                "print('Функция убывает на интервалах Х:')\n",
                "for i in range(len(extremums)-1):\n",
                "    if (extremums[i]['f']) > 0:\n",
                "        print(f'{extremums[i][\"x\"]} -> {extremums[i+1][\"x\"]}')\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "4. Построить график"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "image/png": "iVBORw0KGgoAAAANSUhEUgAAAnYAAAHWCAYAAAD6oMSKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8o6BhiAAAACXBIWXMAAA9hAAAPYQGoP6dpAAByx0lEQVR4nO3deZhU5ZU/8O+tvau7el9YutkFREQQEXdxBaOZmBgTM04MxjFxfujooGPULOjEaCYazcQ4Gjc0iVuMUbOMKAFFURAEEUHZaWgaet+qq7r2+/uj6r1VDb1U3br31tLfz/PwaHdXd126mq5T57znHEmWZRlERERElPNMmb4AIiIiItIGAzsiIiKiPMHAjoiIiChPMLAjIiIiyhMM7IiIiIjyBAM7IiIiojzBwI6IiIgoTzCwIyIiIsoTDOyIiIiI8gQDOyIiIqI8kXJg99577+HLX/4yxowZA0mS8Prrr6f0+XfffTckSTrmT2FhYaqXQkREREQJUg7sPB4PTjrpJDz66KOq7vC2227DkSNH+v2ZMWMGrrzySlVfj4iIiIiiUg7sLrnkEtx777346le/OuDH/X4/brvtNowdOxaFhYWYP38+3n33XeXjRUVFGDVqlPKnubkZn3/+Oa677jrVfwkiIiIi0uGM3Y033oh169bhpZdewtatW3HllVdi0aJF2L1794C3f+qppzB16lScffbZWl8KERER0YiiaWB38OBBLF++HK+88grOPvtsTJ48GbfddhvOOussLF++/Jjb+3w+PP/888zWEREREWnAouUX++yzzxAOhzF16tR+7/f7/aioqDjm9q+99hrcbje+853vaHkZRERERCOSpoFdb28vzGYzNm3aBLPZ3O9jRUVFx9z+qaeewmWXXYaamhotL4OIiIhoRNI0sJszZw7C4TBaWlqGPTO3f/9+vPPOO/jLX/6i5SUQERERjVgpB3a9vb3Ys2eP8vb+/fuxZcsWlJeXY+rUqbj66qtxzTXX4Je//CXmzJmD1tZWrFq1CrNmzcKll16qfN4zzzyD0aNH45JLLtHmb0JEREQ0wkmyLMupfMK7776L884775j3f+c738Gzzz6LYDCIe++9F7/73e/Q2NiIyspKnHbaabjnnntw4oknAgAikQjGjx+Pa665Bj/72c+0+ZsQERERjXApB3ZERERElJ24K5aIiIgoTzCw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",
                        "text/plain": [
                            "<Figure size 640x480 with 1 Axes>"
                        ]
                    },
                    "metadata": {},
                    "output_type": "display_data"
                },
                {
                    "data": {
                        "text/plain": [
                            "<sympy.plotting.plot.Plot at 0x117c32410>"
                        ]
                    },
                    "execution_count": 10,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "\n",
                "from sympy.plotting import plot\n",
                "plot(f, (x, -50, 50))\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "5. Вычислить вершину"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 11,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "Вершины и низины:\n",
                        "\n",
                        "('x:-47.2256484817221', 'f:51965417.3917112')\n",
                        "('x:-44.1199370667845', 'f:-36472120.4544392')\n",
                        "('x:-40.9470735375890', 'f:29526756.9705978')\n",
                        "('x:-37.8313985972732', 'f:-19585603.0827292')\n",
                        "('x:-34.7701099588650', 'f:15303833.9927443')\n",
                        "('x:-31.6407957980140', 'f:-9379044.81523089')\n",
                        "('x:-28.4957796720679', 'f:6971858.35930036')\n",
                        "('x:-25.3466461586162', 'f:-3809649.46040443')\n",
                        "('x:-22.2261972964361', 'f:2619650.03321970')\n",
                        "('x:-19.1455941359425', 'f:-1189637.26151163')\n",
                        "('x:-16.0665525069077', 'f:719768.904596312')\n",
                        "('x:-12.9280559916623', 'f:-230198.503491012')\n",
                        "('x:-9.9337690610358', 'f:107565.823617025')\n",
                        "('x:-6.85062228513275', 'f:-13815.6168035180')\n",
                        "('x:-4.12686592820621', 'f:3106.12673740818')\n",
                        "('x:1.66103336072289', 'f:-73.8651267078111')\n",
                        "('x:3.77305684575625', 'f:868.742609444956')\n",
                        "('x:6.98352369796896', 'f:-25605.2595635028')\n",
                        "('x:9.83516413341352', 'f:72552.0295914994')\n",
                        "('x:13.0606499895942', 'f:-308338.756647110')\n",
                        "('x:16.0405848102516', 'f:571107.225771733')\n",
                        "('x:19.1928480700451', 'f:-1441800.87289197')\n",
                        "('x:22.1926000632169', 'f:2222971.95326252')\n",
                        "('x:25.3988388764551', 'f:-4396121.39457130')\n",
                        "('x:28.4590297922122', 'f:6139826.42798095')\n",
                        "('x:31.5952429281633', 'f:-10520090.2668305')\n",
                        "('x:34.7317612356933', 'f:13801250.8934478')\n",
                        "('x:37.8870621935254', 'f:-21538694.9863683')\n",
                        "('x:41.0078043212952', 'f:27064637.3122280')\n",
                        "('x:44.0763314152199', 'f:-39532981.8548179')\n",
                        "('x:47.2858013946050', 'f:48163046.5224163')\n",
                        "('x:49.0640356793606', 'f:-26676277.9861226')\n",
                        "('x:50.4396400840685', 'f:-67013825.4657204')\n"
                    ]
                }
            ],
            "source": [
                "print('Вершины и низины:\\n', *[('x:'+str(e['x']), 'f:' + str(e['f'])) for e in extremums], sep='\\n')\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "6. Определить промежутки, на котором f > 0"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 12,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "('-48.7256484817221', '-45.5199370667845')\n",
                        "('-42.4470735375890', '-39.2313985972732')\n",
                        "('-36.1701099588650', '-32.9407957980140')\n",
                        "('-29.8957796720679', '-26.6466461586162')\n",
                        "('-23.6261972964361', '-20.3455941359425')\n",
                        "('-17.3665525069077', '-14.0280559916623')\n",
                        "('-11.1337690610358', '-7.65062228513275')\n",
                        "('-5.02686592820621', '-1.33896663927711')\n",
                        "('2.27305684575625', '4.38352369796896')\n",
                        "('8.03516413341352', '10.8606499895942')\n",
                        "('14.2405848102516', '17.1928480700451')\n",
                        "('20.4926000632169', '23.4988388764551')\n",
                        "('26.7590297922122', '29.7952429281633')\n",
                        "('33.0317612356933', '36.0870621935254')\n",
                        "('39.3078043212952', '42.3763314152199')\n",
                        "('45.5858013946050', '48.6640356793606')\n"
                    ]
                }
            ],
            "source": [
                "print(*[(str(r[0]), str(r[1])) for r in f_positive_ranges], sep='\\n')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "7. Определить промежутки, на котором f < 0"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 13,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "('-45.5199370667845', '-42.4470735375890')\n",
                        "('-39.2313985972732', '-36.1701099588650')\n",
                        "('-32.9407957980140', '-29.8957796720679')\n",
                        "('-26.6466461586162', '-23.6261972964361')\n",
                        "('-20.3455941359425', '-17.3665525069077')\n",
                        "('-14.0280559916623', '-11.1337690610358')\n",
                        "('-7.65062228513275', '-5.02686592820621')\n",
                        "('-1.33896663927711', '2.27305684575625')\n",
                        "('4.38352369796896', '8.03516413341352')\n",
                        "('10.8606499895942', '14.2405848102516')\n",
                        "('17.1928480700451', '20.4926000632169')\n",
                        "('23.4988388764551', '26.7590297922122')\n",
                        "('29.7952429281633', '33.0317612356933')\n",
                        "('36.0870621935254', '39.3078043212952')\n",
                        "('42.3763314152199', '45.5858013946050')\n",
                        "('48.6640356793606', '49.1396400840685')\n",
                        "('49.1396400840685', '51.8650474071078')\n"
                    ]
                }
            ],
            "source": [
                "print(*[(str(r[0]), str(r[1])) for r in f_negative_ranges], sep='\\n')\n"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3.11.0 64-bit",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.0"
        },
        "orig_nbformat": 4,
        "vscode": {
            "interpreter": {
                "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
            }
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}
