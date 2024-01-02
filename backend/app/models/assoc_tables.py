from . import db

wishlist_items_association_table = db.Table(
  "wishlist_items",
  db.Column("wishlist_id", db.Integer, db.ForeignKey("wishlists.id")),
  db.Column("item_id", db.Integer, db.ForeignKey("listings.id"))
)