//
//  ProfileView.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct ProfileView: View {
    @State var networkManager: NetworkManager

    var body: some View {
        VStack {
            Image(systemName: "person.fill")
                .resizable()
                .frame(width: 50, height: 50)
                .padding()
                .foregroundColor(.white)
                .background(LinearGradient(gradient: Gradient(colors: [Color.red, Color.purple]), startPoint: .leading, endPoint: .trailing))
                .cornerRadius(40)
            
            HStack {
                Text(self.networkManager.threadData[0].username.capitalized + " Question History")
                .bold()
                .padding()
            }
            
            List(self.networkManager.userData) { thread in
                NavigationLink(destination: ThreadDetailRow(thread: thread)) {
                    ThreadRow(thread: thread)
                }
            }
            
            Spacer()
        }
    }
}

struct ProfileView_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
        // ProfileView()
    }
}
