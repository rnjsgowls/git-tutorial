{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOo9XNmc0QQY+neojtf6FM6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rnjsgowls/git-tutorial/blob/main/%EC%BB%B4%ED%93%A8%ED%84%B0%EA%B3%BC%ED%95%99%EA%B3%BC%20202510778%20%EA%B6%8C%ED%95%B4%EC%A7%84.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sPjEYre7iyRC",
        "outputId": "345ca407-6b03-40ef-d70a-00e926f6e506"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "넓이를 구하고자 하는 원의 반지름은?4\n",
            "반지름 4 인 원의 넓이 50.24\n"
          ]
        }
      ],
      "source": [
        "prompt=\"넓이를 구하고자 하는 원의 반지름은?\"\n",
        "def get_radius(prompt):\n",
        "  r=int(input(prompt))\n",
        "  return r\n",
        "def get_circle_area():\n",
        "  r=get_radius(prompt)\n",
        "  s=3.14*r*r\n",
        "  print(\"반지름\",r,\"인 원의 넓이\",s)\n",
        "  return s\n",
        "result=get_circle_area()"
      ]
    }
  ]
}