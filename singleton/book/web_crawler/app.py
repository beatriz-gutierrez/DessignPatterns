from image_downloader import ImageDonwloaderThread
import singleton_images
from transverse_site import traverse_site


if __name__ == "__main__":

    url_root = (
        "https://blog.kartones.net/post/js-rle-algorithm-v3-bit-level-rle/"
    )

    singleton_crawler = singleton_images.Singleton(queue_to_parse=[url_root])

    traverse_site()

    # 2 parallel threads
    for n_thread in range(2):
        thread1 = ImageDonwloaderThread(n_thread, f"Thread-{n_thread}", n_thread)
        thread1.run()



