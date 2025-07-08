import numpy as np
import csv

class yt:
    def __init__ (self):
        self.yt_1 = np.array([1, 2, 3, 4, 5])
        self.views = 0
        self.likes = 0
        self.comments = 0
        self.stored_info = []

    def views_allocate(self):
        self.views = np.random.randint(1, 5000)
        return self.views

    def likes_allocate(self):
        self.likes = np.random.randint(1, 100)
        return self.likes

    def comments_allocate(self):
        self.comments = np.random.randint(1, 10)
        return self.comments

    def save_info(self):
        for i in self.yt_1:
            total_views = self.views_allocate()
            total_likes = self.likes_allocate()
            total_comments = self.comments_allocate()


            final_result = self.stored_info.append([i, total_views, total_likes, total_comments])
            # printing the info
            print("Activity Locator:")
            print(f"Video ID: {i}")
            print("Total Views: ",total_views)
            print("Total Likes: ",total_likes)
            print("Total Comments: ", total_comments)
            print("array: ", final_result)



    def export_to_csv(self, filename="yt_data.csv"):
        with open(filename, mode = 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Video ID", "Views", "Likes", "Comments"])
            writer.writerows(self.stored_info)
        print(f"Data exported successfully! to '{filename}'")


my_yt = yt()
my_yt.save_info()
my_yt.export_to_csv()