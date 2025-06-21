from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .harmonic import get_prime_and_harmony

class PrimeView(APIView):
    """
    GET /api/prime/<n>/
    Returns the n-th prime and its harmonic sequence value.
    """
    def get(self, request, n):
        # Validate n
        try:
            n = int(n)
            if n < 1:
                raise ValueError
        except ValueError:
            return Response(
                {'error': 'n must be a positive integer'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Compute
        prime, harmony = get_prime_and_harmony(n)
        return Response({
            'index': n,
            'prime': prime,
            'harmony': harmony
        })
