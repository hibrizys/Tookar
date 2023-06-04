package com.example.barterapp.data

import android.os.Parcel
import android.os.Parcelable

class Offer() : Parcelable {
    var mOfferId: String? = null
    var mToUserId: String? = null
    var mToAlias: String? = null
    var mFromUserId: String? = null
    var mFromAlias: String? = null
    var mProductId: String? = null
    var mProductImgUri: String? = null
    var mContactEmail: String? = null
    var mMessage: String? = null
    var mIsPending = false
    var mIsAccepted = false

    constructor(
        offerId: String?, mToUserId: String?, mToAlias: String?, mFromUserId: String?,
        mFromAlias: String?, mProductId: String?, mProductImgUri: String?, mContactEmail: String?,
        mMessage: String?, mIsPending: Boolean, mIsAccepted: Boolean
    ) : this() {
        this.mOfferId = offerId
        this.mToUserId = mToUserId
        this.mToAlias = mToAlias
        this.mFromUserId = mFromUserId
        this.mFromAlias = mFromAlias
        this.mProductId = mProductId
        this.mProductImgUri = mProductImgUri
        this.mContactEmail = mContactEmail
        this.mMessage = mMessage
        this.mIsPending = mIsPending
        this.mIsAccepted = mIsAccepted
    }

    protected constructor(parcel: Parcel) : this() {
        mOfferId = parcel.readString()
        mToUserId = parcel.readString()
        mToAlias = parcel.readString()
        mFromUserId = parcel.readString()
        mFromAlias = parcel.readString()
        mProductId = parcel.readString()
        mProductImgUri = parcel.readString()
        mContactEmail = parcel.readString()
        mMessage = parcel.readString()
        mIsPending = parcel.readByte().toInt() != 0
        mIsAccepted = parcel.readByte().toInt() != 0
    }

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeString(mOfferId)
        parcel.writeString(mToUserId)
        parcel.writeString(mToAlias)
        parcel.writeString(mFromUserId)
        parcel.writeString(mFromAlias)
        parcel.writeString(mProductId)
        parcel.writeString(mProductImgUri)
        parcel.writeString(mContactEmail)
        parcel.writeString(mMessage)
        parcel.writeByte((if (mIsPending) 1 else 0).toByte())
        parcel.writeByte((if (mIsAccepted) 1 else 0).toByte())
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<Offer> {
        override fun createFromParcel(parcel: Parcel): Offer {
            return Offer(parcel)
        }

        override fun newArray(size: Int): Array<Offer?> {
            return arrayOfNulls(size)
        }
    }
}
