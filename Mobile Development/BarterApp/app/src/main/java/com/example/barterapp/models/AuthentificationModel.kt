//package com.example.barterapp.models
//
//import androidx.annotation.NonNull
//import androidx.lifecycle.MutableLiveData
//import com.example.barterapp.data.Response
//import com.example.barterapp.data.UserProfile
//import com.example.barterapp.utility.DefinesUtility
//import com.google.android.gms.tasks.OnCompleteListener
//import com.google.android.gms.tasks.Task
//import com.google.firebase.auth.AuthResult
//import com.google.firebase.auth.FirebaseAuth
//import com.google.firebase.auth.FirebaseUser
//import com.google.firebase.auth.UserProfileChangeRequest
//import com.google.firebase.firestore.DocumentReference
//import com.google.firebase.firestore.DocumentSnapshot
//import com.google.firebase.firestore.FirebaseFirestore
//import com.example.barterapp.utility.DefinesUtility.*
//
///**
//
//The Authentification model handles the requests and responses for FirebaseAuth and FirebaseFirestore
// */
//class AuthentificationModel {
//    private var mAuth: FirebaseAuth = FirebaseAuth.getInstance()
//    private var mCurrentUser: FirebaseUser? = null
//    private var mDatabase: FirebaseFirestore = FirebaseFirestore.getInstance()
//    private var mLoginResponseLiveData: MutableLiveData<Response> = MutableLiveData()
//    private var mRegisterResponseLiveData: MutableLiveData<Response> = MutableLiveData()
//    private var mResetPassResponseLiveData: MutableLiveData<Response> = MutableLiveData()
//    private var mUserProfileLiceData: MutableLiveData<UserProfile> = MutableLiveData()
//
//    // private constructor : singleton access
//    init {
//        mDatabase = FirebaseFirestore.getInstance()
//        mAuth = FirebaseAuth.getInstance()
//    }
//
//    /**
//
//    Gets instance.
//
//    @return the instance
//     */
//    companion object {
//        @Volatile
//        private var mInstance: AuthentificationModel? = null
//
//        @Synchronized
//        fun getInstance(): AuthentificationModel {
//            if (mInstance == null) {
//                mInstance = AuthentificationModel()
//            }
//            return mInstance!!
//        }
//    }
//
//    /**
//
//    Get mutable live data login response mutable live data.
//    @return the mutable live data
//     */
//    fun getMutableLiveDataLoginResponse(): MutableLiveData<Response> {
//        return mLoginResponseLiveData
//    }
//    /**
//
//    Get mutable live data register response mutable live data.
//    @return the mutable live data
//     */
//    fun getMutableLiveDataRegisterResponse(): MutableLiveData<Response> {
//        return mRegisterResponseLiveData
//    }
//    /**
//
//    Get mutable live data reset pass mutable live data.
//    @return the mutable live data
//     */
//    fun getMutableLiveDataResetPass(): MutableLiveData<Response> {
//        return mResetPassResponseLiveData
//    }
//    /**
//
//    Get mutable live data user profile mutable live data.
//    @return the mutable live data
//     */
//    fun getMutableLiveDataUserProfile(): MutableLiveData<UserProfile> {
//        return mUserProfileLiceData
//    }
//    /**
//
//    Sign in.
//
//    @param email the email
//
//    @param pass the pass
//     */
//    fun signIn(email: String, pass: String) {
//
//        mAuth.signInWithEmailAndPassword(email, pass)
//            .addOnCompleteListener { task: Task<AuthResult?> ->
//                if (task.isSuccessful) {
//// Sign in success
//                    mCurrentUser = mAuth.currentUser
//                    mLoginResponseLiveData.value = Response(SUCC_LOGIN, true)
//                } else {
//// Sign in failed
//                    mLoginResponseLiveData.value = Response(ERR_LOGIN, false)
//                }
//            }
//    }
//
//    /**
//
//    Sign up.
//    @param userProfile the user profile
//    @param pass the pass
//     */
////Registers the a new user according to the profile and password
//    fun signUp(userProfile: UserProfile, pass: String) {
//        mAuth.createUserWithEmailAndPassword(userProfile.mEmail, pass)
//            .addOnCompleteListener { task: Task<AuthResult?> ->
//                if (task.isSuccessful) {
//// Sign up success
//                    mCurrentUser = mAuth.currentUser
//                    mRegisterResponseLiveData.value = Response(SUCC_REGISTER, true)
//                    val uId = mCurrentUser!!.uid
//// Populate the user's profile
//                    mDatabase.collection(USERS_COLLECTION).document(uId).set(userProfile)
////set the display name for the user in
//                    val profileUpdates = UserProfileChangeRequest.Builder()
//                        .setDisplayName(userProfile.mAlias).build()
//                    mCurrentUser!!.updateProfile(profileUpdates)
//                } else {
//// Sign up failed
//                    mRegisterResponseLiveData.value = Response(ERR_REGISTER, false)
//                }
//            }
//    }
//    /**
//
//    Reset password.
//    @param email the email
//     */
////Resets the password on the desired email address
//    fun resetPassword(email: String) {
//        mAuth.sendPasswordResetEmail(email)
//            .addOnCompleteListener { task: Task<Void?> ->
//                if (task.isSuccessful) {
//// mail was sent successfully.
//                    mResetPassResponseLiveData.value = Response(SUCC_RESET_PASS, true)
//                } else {
//                    mResetPassResponseLiveData.value = Response(task.exception!!.message!!, true)
//                }
//            }
//    }
//    /**
//
//    Get user profile boolean.
//
//    @return the boolean
//     */
////Gets the Users Profile
//    fun getUserProfile(): Boolean {
//
////if not signed in, no use of continuing
//        if (!isUserSignedIn()) return false
//
//        val docRef: DocumentReference = mDatabase.collection(USERS_COLLECTION).document(mCurrentUser!!.uid)
//        docRef.get().addOnCompleteListener { task: Task<DocumentSnapshot?> ->
//            if (task.isSuccessful) {
//                val userProfile = task.result!!.toObject(UserProfile::class.java)
//                mUserProfileLiceData.value = userProfile
//            }
////
//        }
//
////request completed successfully
//        return true
//    }
//
//    /**
//
//    Sign out.
//     */
////Signs out from the current user
//    fun signOut() {
//        mAuth.signOut()
//    }
//    /**
//
//    Get user email string.
//    @return the string
//     */
//    fun getUserEmail(): String {
//        var userEmail = "anonymous@user.com"
//        if (null != mAuth.currentUser) {
//            userEmail = mAuth.currentUser!!.email!!
//        }
//        return userEmail
//    }
//    /**
//
//    Get user alias string.
//    @return the string
//     */
//    fun getUserAlias(): String {
//        var userAlias = "anonymous"
//        if (null != mAuth.currentUser) {
//            userAlias = mAuth.currentUser!!.displayName!!
//        }
//        return userAlias
//    }
//    /**
//
//    Is user signed in boolean.
//    @return the boolean
//     */
//    fun isUserSignedIn(): Boolean {
//        return mAuth.currentUser != null
//    }
//    /**
//
//    Gets current user id.
//    @return the current user id
//     */
//    fun getCurrentUserId(): String {
//        return mAuth.currentUser!!.uid
//    }
//}