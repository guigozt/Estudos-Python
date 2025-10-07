numCasos = int(input())

for i in range(numCasos):
    v1, v2, v3 = map(float, input().split())
    
    mediaV1 = v1 * 2
    mediaV2 = v2 * 3
    mediaV3 = v3 * 5
    mediaTotal = (mediaV1 + mediaV2 + mediaV3) / 10
    
    print(f'{mediaTotal:.1f}')
