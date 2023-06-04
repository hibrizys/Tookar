
package com.example.barterapp.data

import com.google.firebase.database.IgnoreExtraProperties

/**

The entity User profile.
 */
@IgnoreExtraProperties
class UserProfile {
    var mFirstName: String? = null
    var mSurname: String? = null
    var mTelNo: String? = null
    var mAlias: String? = null
    var mEmail: String? = null

    /**

    Instantiates a new User profile.
     */
    constructor() {}
    /**

    Instantiates a new User profile.
    @param mFirstName the m first name
    @param mSurname the m surname
    @param mTelNo the m tel no
    @param mAlias the m alias
    @param mEmail the m email
     */
    constructor(
        mFirstName: String?,
        mSurname: String?,
        mTelNo: String?,
        mAlias: String?,
        mEmail: String?
    ) {
        this.mFirstName = mFirstName
        this.mSurname = mSurname
        this.mTelNo = mTelNo
        this.mAlias = mAlias
        this.mEmail = mEmail
    }
    /**

    Gets first name.
    @return the first name
     */
    fun getmFirstName(): String? {
        return mFirstName
    }
    /**

    Gets surname.
    @return the surname
     */
    fun getmSurname(): String? {
        return mSurname
    }
    /**

    Gets tel no.
    @return the tel no
     */
    fun getmTelNo(): String? {
        return mTelNo
    }
    /**

    Gets alias.
    @return the alias
     */
    fun getmAlias(): String? {
        return mAlias
    }
    /**

    Gets email.
    @return the email
     */
    fun getmEmail(): String? {
        return mEmail
    }
    /**

    Sets first name.
    @param mFirstName the m first name
     */
    fun setmFirstName(mFirstName: String?) {
        this.mFirstName = mFirstName
    }
    /**

    Sets surname.
    @param mSurname the m surname
     */
    fun setmSurname(mSurname: String?) {
        this.mSurname = mSurname
    }
    /**

    Sets tel no.
    @param mTelNo the m tel no
     */
    fun setmTelNo(mTelNo: String?) {
        this.mTelNo = mTelNo
    }
    /**

    Sets alias.
    @param mAlias the m alias
     */
    fun setmAlias(mAlias: String?) {
        this.mAlias = mAlias
    }
    /**

    Sets email.
    @param mEmail the m email
     */
    fun setmEmail(mEmail: String?) {
        this.mEmail = mEmail
    }
}