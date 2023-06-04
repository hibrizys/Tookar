package com.example.barterapp.data

import android.os.Parcel
import android.os.Parcelable

/**
 * The Product entity.
 */
class Product() : Parcelable {
    var mUserId: String? = null
    var mProductId: String? = null
    var mAlias: String? = null
    var mTitle: String? = null
    var mDescription: String? = null
    var mCategory: String? = null
    var mImgUri: String? = null
    var mVidUri: String? = null
    var mTimeStamp: Long = 0

    /**
     * Instantiates a new Product.
     *
     * @param mUserId      the m user id
     * @param productId    the product id
     * @param alias        the alias
     * @param mTitle       the m title
     * @param mDescription the m description
     * @param mCategory    the m category
     * @param imgUri       the img uri
     * @param vidUri       the vid uri
     * @param timeStamp    the time stamp
     */
    constructor(
        mUserId: String?,
        productId: String?,
        alias: String?,
        mTitle: String?,
        mDescription: String?,
        mCategory: String?,
        imgUri: String?,
        vidUri: String?,
        timeStamp: Long
    ) : this() {
        this.mUserId = mUserId
        this.mProductId = productId
        this.mAlias = alias
        this.mTitle = mTitle
        this.mDescription = mDescription
        this.mCategory = mCategory
        this.mImgUri = imgUri
        this.mVidUri = vidUri
        this.mTimeStamp = timeStamp
    }

    /**
     * Instantiates a new Product.
     *
     * @param in the in
     */
    protected constructor(parcel: Parcel) : this() {
        mUserId = parcel.readString()
        mProductId = parcel.readString()
        mAlias = parcel.readString()
        mTitle = parcel.readString()
        mDescription = parcel.readString()
        mCategory = parcel.readString()
        mImgUri = parcel.readString()
        mVidUri = parcel.readString()
        mTimeStamp = parcel.readLong()
    }

    /**
     * The constant CREATOR.
     */
    // this is used to regenerate your object. All Parcelables must have a CREATOR that implements these two methods
    companion object CREATOR : Parcelable.Creator<Product> {
        override fun createFromParcel(parcel: Parcel): Product {
            return Product(parcel)
        }

        override fun newArray(size: Int): Array<Product?> {
            return arrayOfNulls(size)
        }
    }

    override fun describeContents(): Int {
        return 0
    }

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeString(mUserId)
        parcel.writeString(mProductId)
        parcel.writeString(mAlias)
        parcel.writeString(mTitle)
        parcel.writeString(mDescription)
        parcel.writeString(mCategory)
        parcel.writeString(mImgUri)
        parcel.writeString(mVidUri)
        parcel.writeLong(mTimeStamp)
    }
}
