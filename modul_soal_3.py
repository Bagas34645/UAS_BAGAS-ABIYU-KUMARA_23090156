# queue.py

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' telah ditambahkan ke antrian.")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"Pesanan '{removed_item}' telah dihapus dari antrian.")
            return removed_item
        else:
            print("Antrian kosong, tidak ada pesanan untuk dihapus.")

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("Pesanan dalam antrian:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("Antrian kosong.")
