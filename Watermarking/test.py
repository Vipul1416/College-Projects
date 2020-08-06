from watermarking import watermarking
watermarking = watermarking()
watermarking.watermark(img="lena.jpg", path_save=None)
watermarking.extracted(image_path="watermarked_lena.jpg",extracted_watermark_path = None)
