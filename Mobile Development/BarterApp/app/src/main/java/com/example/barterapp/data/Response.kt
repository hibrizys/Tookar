package com.example.barterapp.data

/**
 * The entity Response.
 */
class Response(var mResponseText: String, var mIsSuccessfull: Boolean) {

    /**
     * Gets is successfull.
     *
     * @return the is successfull
     */
    fun getIsSuccessfull(): Boolean {
        return mIsSuccessfull
    }

    /**
     * Sets is successfull.
     *
     * @param isSuccessfull the is successfull
     */
    fun setIsSuccessfull(isSuccessfull: Boolean) {
        mIsSuccessfull = isSuccessfull
    }

    /**
     * Gets response text.
     *
     * @return the response text
     */
    fun getResponseText(): String {
        return mResponseText
    }

    /**
     * Sets response text.
     *
     * @param responseText the response text
     */
    fun setResponseText(responseText: String) {
        mResponseText = responseText
    }
}
