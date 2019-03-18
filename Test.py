# encoding: utf8

from PIL import Image, ImageChops
from skimage import io, filters, color
from skimage.measure import compare_ssim

# average array
average = color.rgb2gray((io.imread("11_100_edges.jpg")))
averageImage = Image.fromarray(average)
averageImage.show()
average = average / 255

# original to grey part 1
i = 10
while i < 32:
    z = "{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    print("Opened: ", z)
    arrGrey = Image.fromarray(img1 * 255)
    # saving grey as image
    if arrGrey.mode != 'RGB':
        arrGrey = arrGrey.convert('L')
    arrGrey.save("{}_100_grey.jpg".format(i))
    # filter
    edges = filters.roberts(arrGrey)
    # summ with average
    average += edges

    # # difference
    # imgRob = io.imread("10_100_edges.jpg")
    # imgRob1 = io.imread("{}_100_edges.jpg".format(i))
    # (score, diff) = compare_ssim(imgRob1, imgRob, full=True, multichannel=False)
    # diff = (diff * 255).astype("uint8")
    # print("SSIM: {}".format(score))
    # diff = Image.fromarray(diff * 255)
    # if diff.mode != 'RGB':
    #     diff = diff.convert('L')
    # diff.save("10_{}_100_diff.jpg".format(i))
    # # image from array and saving image
    # edgesImg = Image.fromarray(edges * 255)
    # if edgesImg.mode != 'RGB':
    #     edgesImg = edgesImg.convert('L')
    #     edgesImg.save("{}_100_edges.jpg".format(i))

    i += 1
# original to grey part 2
i = 100
while i < 321:
    z = "{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    print("Opened: ", z)
    arrGrey = Image.fromarray(img1 * 255)
    # saving grey as image
    if arrGrey.mode != 'RGB':
        arrGrey = arrGrey.convert('L')
    arrGrey.save("{}_100_grey.jpg".format(i))
    # filter
    edges = filters.roberts(arrGrey)
    # summ with average
    average += edges

    # # difference
    # imgRob = io.imread("10_100_edges.jpg")
    # imgRob1 = io.imread("{}_100_edges.jpg".format(i))
    # (score, diff) = compare_ssim(imgRob1, imgRob, full=True, multichannel=False)
    # diff = (diff * 255).astype("uint8")
    # print("SSIM: {}".format(score))
    #
    # diff = Image.fromarray(diff * 255)
    # if diff.mode != 'RGB':
    #     diff = diff.convert('L')
    # diff.save("10_{}_100_diff.jpg".format(i))
    # # image from array and saving image
    # edgesImg = Image.fromarray(edges * 255)
    # if edgesImg.mode != 'RGB':
    #     edgesImg = edgesImg.convert('L')
    #     edgesImg.save("{}_100_edges.jpg".format(i))

    i += 1

# show average
average = average / 241
averageImage = Image.fromarray(average * 255)
if averageImage.mode != 'RGB':
    averageImage = averageImage.convert('L')
averageImage.save("average_apple_golden_2.jpg")
averageImage.show()

# average for gorizontal images
averageGor = color.rgb2gray((io.imread("r_0_100_edges.jpg")))
averageGorImage = Image.fromarray(averageGor)
averageGorImage.show()
averageGor = averageGor / 255

# original to grey part 1
i = 10
while i < 32:
    z = "r_{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    print("Opened: ", z)
    arrGrey = Image.fromarray(img1 * 255)
    # saving grey as image
    if arrGrey.mode != 'RGB':
        arrGrey = arrGrey.convert('L')
    arrGrey.save("r_{}_100_grey.jpg".format(i))
    # filter
    edges = filters.roberts(arrGrey)
    # summ with average
    averageGor += edges
    i += 1

# original to grey part 2
i = 100
while i < 321:
    z = "r_{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    print("Opened: ", z)
    arrGrey = Image.fromarray(img1 * 255)
    # saving grey as image
    if arrGrey.mode != 'RGB':
        arrGrey = arrGrey.convert('L')
    arrGrey.save("r_{}_100_grey.jpg".format(i))
    # filter
    edges = filters.roberts(arrGrey)
    # summ with average
    averageGor += edges
    i += 1

# show average gorizontal
averageGor = averageGor / 241
averageGorImage = Image.fromarray(averageGor * 255)
if averageGorImage.mode != 'RGB':
    averageGorImage = averageGorImage.convert('L')
averageGorImage.save("average_gorizopntal_apple_golden_2.jpg")
averageGorImage.show()

# average array for pomegranate
averagePom = color.rgb2gray((io.imread("Pomegranate/32_100_edges.jpg")))
averageImage = Image.fromarray(averagePom)
averageImage.show()
averagePom = averagePom / 255

# original to grey part 1
i = 32
while i < 100:
    z = "Pomegranate/{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    print("Opened: ", z)
    arrGrey = Image.fromarray(img1 * 255)
    # saving grey as image
    if arrGrey.mode != 'RGB':
        arrGrey = arrGrey.convert('L')
    arrGrey.save("Pomegranate/{}_100_grey.jpg".format(i))
    # filter
    edges = filters.roberts(arrGrey)
    # summ with average
    averagePom += edges
    i += 1
# original to grey part 2
i = 321
while i < 328:
    z = "Pomegranate/{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    print("Opened: ", z)
    arrGrey = Image.fromarray(img1 * 255)
    # saving grey as image
    if arrGrey.mode != 'RGB':
        arrGrey = arrGrey.convert('L')
    arrGrey.save("Pomegranate/{}_100_grey.jpg".format(i))
    # filter
    edges = filters.roberts(arrGrey)
    # summ with average
    averagePom += edges
    i += 1
# show average pomegranate
averagePom = averagePom / 79
averagePomImage = Image.fromarray(averagePom * 255)
if averagePomImage.mode != 'RGB':
    averagePomImage = averagePomImage.convert('L')
averagePomImage.save("Pomegranate/average_pomagranate.jpg")
averagePomImage.show()

# TESTING
print("TESTING")
amountAll = 241
amountBad = 0
# Apple vertical
i = 10
while i < 32:
    z = "Training/Apple/{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    arrGrey = Image.fromarray(img1 * 255)
    # filter
    imgAppleCurrent = filters.roberts(arrGrey)
    # compare
    imgAverage = io.imread("average_apple_golden_2.jpg")
    (scoreApple, diff) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple vertical: {}".format(scoreApple))
    # compare
    imgAverage = io.imread("average_gorizopntal_apple_golden_2.jpg")
    (scoreAppleGor, diff1) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple gorizontal: {}".format(scoreAppleGor))
    # compare
    imgAverage = io.imread("Pomegranate/average_pomegranate.jpg")
    (scorePomegranate, diff2) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Pomegranate: {}".format(scorePomegranate))
    i += 1

if (scorePomegranate > scoreApple):
    if (scorePomegranate > scoreAppleGor):
        amountBad += 1
i = 100
while i < 321:
    z = "Training/Apple/{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    arrGrey = Image.fromarray(img1 * 255)
    # filter
    imgAppleCurrent = filters.roberts(arrGrey)
    # compare
    imgAverage = io.imread("average_apple_golden_2.jpg")
    (scoreApple, diff) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple vertical: {}".format(scoreApple))
    # compare
    imgAverage = io.imread("average_gorizopntal_apple_golden_2.jpg")
    (scoreAppleGor, diff1) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple gorizontal: {}".format(scoreAppleGor))
    # compare
    imgAverage = io.imread("Pomegranate/average_pomegranate.jpg")
    (scorePomegranate, diff2) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Pomegranate: {}".format(scorePomegranate))
    i += 1

if (scorePomegranate > scoreApple):
    if (scorePomegranate > scoreAppleGor):
        amountBad += 1

# Apple gorizontal
print("AFTER APPLE VERTICAL, AMOUNT BAD: ", amountBad)
i = 10
while i < 32:
    z = "Training/Apple/r_{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    arrGrey = Image.fromarray(img1 * 255)
    # filter
    imgAppleCurrent = filters.roberts(arrGrey)
    # compare
    imgAverage = io.imread("average_apple_golden_2.jpg")
    (scoreApple, diff) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple vertical: {}".format(scoreApple))
    # compare
    imgAverage = io.imread("average_gorizopntal_apple_golden_2.jpg")
    (scoreAppleGor, diff1) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple gorizontal: {}".format(scoreAppleGor))
    # compare
    imgAverage = io.imread("Pomegranate/average_pomegranate.jpg")
    (scorePomegranate, diff2) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Pomegranate: {}".format(scorePomegranate))
    i += 1

if (scorePomegranate > scoreApple):
    if (scorePomegranate > scoreAppleGor):
        amountBad += 1
i = 100
while i < 321:
    z = "Training/Apple/r_{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    arrGrey = Image.fromarray(img1 * 255)
    # filter
    imgAppleCurrent = filters.roberts(arrGrey)
    # compare
    imgAverage = io.imread("average_apple_golden_2.jpg")
    (scoreApple, diff) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple vertical: {}".format(scoreApple))
    # compare
    imgAverage = io.imread("average_gorizopntal_apple_golden_2.jpg")
    (scoreAppleGor, diff1) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple gorizontal: {}".format(scoreAppleGor))
    # compare
    imgAverage = io.imread("Pomegranate/average_pomegranate.jpg")
    (scorePomegranate, diff2) = compare_ssim(imgAppleCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Pomegranate: {}".format(scorePomegranate))
    i += 1

if (scorePomegranate > scoreApple):
    if (scorePomegranate > scoreAppleGor):
        amountBad += 1
print("AFTER APPLE GORIZONTAL, AMOUNT BAD: ", amountBad)

# Pomegranate
i = 10
while i < 31:
    z = "Training/Pomegranate/{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    arrGrey = Image.fromarray(img1 * 255)
    # filter
    imgCurrent = filters.roberts(arrGrey)
    # compare
    imgAverage = io.imread("average_apple_golden_2.jpg")
    (scoreApple, diff) = compare_ssim(imgCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple vertical: {}".format(scoreApple))
    # compare
    imgAverage = io.imread("average_gorizopntal_apple_golden_2.jpg")
    (scoreAppleGor, diff1) = compare_ssim(imgCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple gorizontal: {}".format(scoreAppleGor))
    # compare
    imgAverage = io.imread("Pomegranate/average_pomegranate.jpg")
    (scorePomegranate, diff2) = compare_ssim(imgCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Pomegranate: {}".format(scorePomegranate))
    i += 1

if (scorePomegranate > scoreApple):
    if (scorePomegranate > scoreAppleGor):
        amountBad += 0
    else:
        amountBad += 1
else:
    amountBad += 1
i = 100
while i < 321:
    z = "Training/Pomegranate/{}_100.jpg".format(i)
    img1 = color.rgb2gray(io.imread(z))
    arrGrey = Image.fromarray(img1 * 255)
    # filter
    imgCurrent = filters.roberts(arrGrey)
    # compare
    imgAverage = io.imread("average_apple_golden_2.jpg")
    (scoreApple, diff) = compare_ssim(imgCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple vertical: {}".format(scoreApple))
    # compare
    imgAverage = io.imread("average_gorizopntal_apple_golden_2.jpg")
    (scoreAppleGor, diff1) = compare_ssim(imgCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Apple gorizontal: {}".format(scoreAppleGor))
    # compare
    imgAverage = io.imread("Pomegranate/average_pomegranate.jpg")
    (scorePomegranate, diff2) = compare_ssim(imgCurrent, imgAverage, full=True, multichannel=False)
    print("SSIM Pomegranate: {}".format(scorePomegranate))
    i += 1

if (scorePomegranate > scoreApple):
    if (scorePomegranate > scoreAppleGor):
        amountBad += 0
    else:
        amountBad += 1
else:
    amountBad += 1
print("AFTER POMEGRANATE, AMOUNT BAD: ", amountBad)
